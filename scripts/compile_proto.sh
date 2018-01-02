#!/usr/bin/env bash
set -e

proto_dir=$GOPATH/src/github.com/kube-message/proto
app_dir=$GOPATH/src/github.com/kube-message/api/api
messenger_python_out_dir=$app_dir/proto/messenger
alerts_python_out_dir=$app_dir/proto/alerts
messenger_venv=$GOPATH/src/github.com/kube-message/api/venv

$messenger_venv/bin/python \
    -m grpc_tools.protoc \
    -I $proto_dir \
    --python_out=$alerts_python_out_dir \
    --grpc_python_out=$alerts_python_out_dir \
    $proto_dir/alerts.proto

$messenger_venv/bin/python \
    -m grpc_tools.protoc \
    -I $proto_dir \
    --python_out=$messenger_python_out_dir \
    --grpc_python_out=$messenger_python_out_dir \
    $proto_dir/messenger.proto
